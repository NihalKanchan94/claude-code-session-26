// Workshop note: no loading state, no error handling, and the bar chart
// is redrawn from scratch every time. No date or region filters yet.

function money(value) {
  return "$" + Math.round(value).toLocaleString();
}

function drawBars(containerId, entries) {
  var container = document.getElementById(containerId);
  container.innerHTML = "";
  var max = 0;
  for (var i = 0; i < entries.length; i++) {
    if (entries[i][1] > max) max = entries[i][1];
  }
  for (var j = 0; j < entries.length; j++) {
    var row = document.createElement("div");
    row.className = "bar-row";
    var label = document.createElement("span");
    label.className = "bar-label";
    label.textContent = entries[j][0];
    var track = document.createElement("div");
    track.className = "bar-track";
    var fill = document.createElement("div");
    fill.className = "bar-fill";
    fill.style.width = (entries[j][1] / max * 100) + "%";
    track.appendChild(fill);
    var value = document.createElement("span");
    value.className = "bar-value";
    value.textContent = money(entries[j][1]);
    row.appendChild(label);
    row.appendChild(track);
    row.appendChild(value);
    container.appendChild(row);
  }
}

fetch("/api/summary")
  .then(function (r) { return r.json(); })
  .then(function (data) {
    document.getElementById("kpi-revenue").textContent = money(data.total_revenue);
    document.getElementById("kpi-orders").textContent = data.order_count;
    document.getElementById("kpi-average").textContent = money(data.average_order);

    drawBars("chart-month", Object.entries(data.by_month));
    drawBars("chart-region", Object.entries(data.by_region));

    var body = document.querySelector("#table-reps tbody");
    data.top_reps.forEach(function (pair) {
      var tr = document.createElement("tr");
      tr.innerHTML = "<td>" + pair[0] + "</td><td>" + money(pair[1]) + "</td>";
      body.appendChild(tr);
    });
  });
