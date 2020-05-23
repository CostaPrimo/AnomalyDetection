var options = {
          series: [
        ],
          chart: {
          id: 'mychart',
          height: 1000,
          type: 'heatmap',
        },
        plotOptions: {
          heatmap: {
            shadeIntensity: 0.5,
            radius: 0,
            useFillColorAsStroke: true,
            colorScale: {
              ranges: [{
                  from: -1,
                  to: 0,
                  name: 'None',
                  color: '#00A100'
                },
                {
                  from: 1,
                  to: 10,
                  name: 'Low',
                  color: '#FFFF00'
                },
                {
                  from: 11,
                  to: 30,
                  name: 'Medium',
                  color: '#FFA500'
                },
                {
                  from: 31,
                  to: 2000,
                  name: 'extreme',
                  color: '#FF0000'
                }
              ]
            }
          }
        },
        dataLabels: {
          enabled: false
        },
        stroke: {
          width: 1
        },
        title: {
          text: 'HeatMap of Anomalies'
        },
        };


        //Gammel metode til at create random data til heatmappet
      function generateData(count, yrange) {
      var i = 0;
      var series = [];
      while (i < count) {
        var x = (i + 1).toString();
        var y = Math.floor(Math.random() * (yrange.max - yrange.min + 1)) + yrange.min;
        series.push({
          x: x,
          y: y
        });
        i++;
      }
      return series;
    }

    var hetmapon = false;
    function heatmap(streamdata){
      var dict = {} 
      dict = streamdata
      var data1 = []
      var series1 = []
       var i = 0;
       var t = 0;
      for (var key in dict) { 
        dist = dict[key]
        i = 0
        t = 0
        while (i < dist.length) {
          dist2 = dist[Object.keys(dist)[t]]
          x = dist2[Object.keys(dist2)[0]]
          y = dist2[Object.keys(dist2)[1]]
          series1.push({
            x: x,
            y: y
          });
          i++;
          t++;
        } 
        data1.push({
          name: key,
          data: series1
        });
        series1 = []
      }

      options.series = data1
      console.log(data1)
      var chart = new ApexCharts(document.querySelector("#chart"), options);
    
      chart.render()
      hetmapon = true

    }




    