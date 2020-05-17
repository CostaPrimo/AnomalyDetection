var options = {
          series: [{
            name: 'Jan',
            data: generateData(20, {
              min: -30,
              max: 55
            })
          },
          {
            name: 'Feb',
            data: generateData(20, {
              min: -30,
              max: 55
            })
          },
          {
            name: 'Mar',
            data: generateData(20, {
              min: -30,
              max: 55
            })
          },
          {
            name: 'Apr',
            data: generateData(20, {
              min: -30,
              max: 55
            })
          },
          {
            name: 'May',
            data: generateData(20, {
              min: -30,
              max: 55
            })
          },
          {
            name: 'Jun',
            data: generateData(20, {
              min: -30,
              max: 55
            })
          },
          {
            name: 'Jul',
            data: generateData(20, {
              min: -30,
              max: 55
            })
          },
          {
            name: 'Aug',
            data: generateData(20, {
              min: -30,
              max: 55
            })
          },
          {
            name: 'Sep',
            data: generateData(20, {
              min: -30,
              max: 55
            })
          }
        ],
          chart: {
          id: 'mychart',
          height: 350,
          type: 'heatmap',
        },
        plotOptions: {
          heatmap: {
            shadeIntensity: 0.5,
            radius: 0,
            useFillColorAsStroke: true,
            colorScale: {
              ranges: [{
                  from: -30,
                  to: 5,
                  name: 'low',
                  color: '#00A100'
                },
                {
                  from: 6,
                  to: 20,
                  name: 'medium',
                  color: '#128FD9'
                },
                {
                  from: 21,
                  to: 45,
                  name: 'high',
                  color: '#FFB200'
                },
                {
                  from: 46,
                  to: 55,
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
          text: 'HeatMap Chart with Color Range'
        },
        };

        var options2 = {
          chart: {
            type: 'line'
          },
          series: [{
            name: 'sales',
            data: [30,40,35,50,49,60,70,91,125]
          }],
          xaxis: {
            categories: [1991,1992,1993,1994,1995,1996,1997, 1998,1999]
          }
        }


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

    function heatmap(streamdata){
      console.log(streamdata)
      //console.log(options)
      //var chart = new ApexCharts(document.querySelector("#chart"), options);
      //chart.render()
    }




    