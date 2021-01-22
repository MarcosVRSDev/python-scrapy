var dadosJSON = [
  {
    "key": "Palavras",
    "color": "#1f77b4",
    "values": []
  }
];

var dados = [];

fetch("../data.json")
  .then(function (resp) {
    return resp.json();
  })
  .then(function (data) {
    Object.keys(data).forEach(element => {
      dados.push({
        "label": element,
        "value": data[element],
        "color": generateRandomColor()
      });
    });
  })
  .finally(function () {
    dadosJSON[0].values = dados;

    nv.addGraph(function () {
      var chart = nv.models.pieChart()
        .x(function (d) {
          return d.label;
        })
        .y(function (d) {
          return d.value;
        })
        .margin({
          top: 30,
          right: 20,
          bottom: 50,
          left: 85
        })
        .showLabels(false)
        .showLegend(false);

      d3.select('#graphMultiBar svg')
        .datum(dadosJSON[0].values)
        .transition().duration(500)
        .call(chart);

      nv.utils.windowResize(chart.update);

      return;
    });
  });

function generateRandomColor() {
  var letters = '0123456789ABCDEF';
  var color = '#';
  for (var i = 0; i < 6; i++) {
    color += letters[Math.floor(Math.random() * 16)];
  }
  return color;
}
