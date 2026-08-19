const url = document.getElementById("url").textContent;
const visContainer = document.getElementById("vis-container");

function titleFromKey(key) {
  return key
    .split("_")
    .map((word) => word.charAt(0).toUpperCase() + word.slice(1))
    .join(" ");
}

const PALETTE = [
  "rgba(54, 162, 235, 0.6)",
  "rgba(255, 99, 132, 0.6)",
  "rgba(255, 206, 86, 0.6)",
  "rgba(75, 192, 192, 0.6)",
  "rgba(153, 102, 255, 0.6)",
];

function renderChart(key, rows) {
  const col = document.createElement("div");
  col.className = "col-12 col-lg-6 mb-4";

  const heading = document.createElement("h2");
  heading.textContent = titleFromKey(key);
  heading.className = "text-center";
  heading.style.cursor = "pointer";
  heading.title = "Click to toggle fullscreen";
  col.appendChild(heading);

  const chartBox = document.createElement("div");
  chartBox.style.height = "400px";
  chartBox.style.backgroundColor = "#fff";
  col.appendChild(chartBox);

  const canvas = document.createElement("canvas");
  chartBox.appendChild(canvas);
  visContainer.appendChild(col);

  heading.addEventListener("click", () => {
    if (document.fullscreenElement === chartBox) {
      document.exitFullscreen();
    } else {
      chartBox.requestFullscreen();
    }
  });
  chartBox.addEventListener("fullscreenchange", () => {
    chartBox.style.height = document.fullscreenElement === chartBox ? "100vh" : "400px";
    chart.resize();
  });

  const isPie = rows.length <= 5;

  const chart = new Chart(canvas, {
    type: isPie ? "pie" : "bar",
    data: {
      labels: rows.map((row) => row.label),
      datasets: [
        {
          label: "count",
          data: rows.map((row) => row.count),
          backgroundColor: isPie
            ? rows.map((_, i) => PALETTE[i % PALETTE.length])
            : "rgba(54, 162, 235, 0.6)",
        },
      ],
    },
    options: {
      responsive: true,
      maintainAspectRatio: false,
      plugins: {
        legend: { display: isPie },
        title: { display: false },
      },
      scales: isPie
        ? {}
        : {
            y: { beginAtZero: true, ticks: { precision: 0 } },
          },
    },
  });
}

fetch(url)
  .then((response) => {
    if (!response.ok) {
      throw new Error("something wrong with the data");
    }
    return response.json();
  })
  .then((data) => {
    Object.entries(data).forEach(([key, rows]) => renderChart(key, rows));
  })
  .catch((error) => {
    console.error("Something went wrong:", error);
  });
