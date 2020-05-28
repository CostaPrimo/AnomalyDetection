var options = {
          series: [
        ],
          chart: {
          id: 'mychart',
          height: 2500,
          width: '100%',
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
        xaxis: {
           rotateAlways: true
        },
        yaxis: {
            labels: {
               minWidth: 0,
               maxWidth: 240,
               offsetY: 5
            },
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
    //Takes the data recieved from the Flask backend, and sets it up into a format that the heatmaps options can read
    function setUpData(streamdatas){
      var dict = {} 
      dict = streamdatas
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
      return data1
    }

    function timeinterval(streamdata1, time){
      data1 = streamdata1
      var n = 0;
      heatmapdata = []
      heatmapArrayData = []
      for (var key in data1) {
        temporary = data1[key] 
        currentStreamName = temporary[Object.keys(temporary)[0]]
        currentStreamData = temporary[Object.keys(temporary)[1]]
        n = 0;  
        while (n < time + 1){
          heatmapArrayData.push(currentStreamData[n])
          n++
        }
        heatmapdata.push({
          name: currentStreamName,
          data: heatmapArrayData
        });
        heatmapArrayData = []
      }
      return heatmapdata
    }

    function heatmap(streamdata){
      //creating the chart
      var chart = new ApexCharts(document.querySelector("#chart"), options);

      var data = setUpData(streamdata)
      console.log(data)

      data1 = data[0]
      length = data1[Object.keys(data1)[1]].length
      
      var intervalData = []
      var i = 0;
      var interval = setInterval(() => {
        if (i < length) {
          intervalData = timeinterval(data, i)
          if (i == 0) {
            options.series = intervalData
            chart.render()
          }
          else{
            chart.updateSeries(intervalData)
          }
        }
        else if(i > length) {
          clearInterval(interval)
          console.log("Interval closed")
        }
        i++
      }, 15000);
    }





    