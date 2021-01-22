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
        "value": data[element]
      });
    });
  })
  .finally(function () {
    dadosJSON[0].values = dados;

    nv.addGraph(function () {
      var chart = nv.models.multiBarChart()
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
        .showControls(false)
        .staggerLabels(true)
        .stacked(true)
        .showXAxis(false);

      chart.xAxis
        .axisLabel('Palavras');

      chart.yAxis
        .tickFormat(d3.format('0f'));

      d3.select('#graphMultiBar svg')
        .datum(dadosJSON)
        .transition().duration(500)
        .call(chart);

      nv.utils.windowResize(chart.update);

      return;
    });
  });
