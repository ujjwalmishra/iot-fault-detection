// const loadData = () => {
//   fetch('/api/v1/usage')
//     .then( response => {
//       if (response.status !== 200) {
//         console.log(response);
//       }
//       return response;
//     })
//     .then(response => response.json())
//     .then(parsedResponse => {
//       const unpackData = (arr, key) => {
//         return arr.map(obj => obj[key])
//       }
//       const firstTrace = {
//         type: 'scatter',
//         mode: 'lines',
//         name: 'Mean User Usage',
//         x: unpackData(parsedResponse, 'time'),
//         y: unpackData(parsedResponse, 'mean_usage_user'),
//         line: {color: '#17BECF'}
//       }
//       const secondTrace = {
//         type: "scatter",
//         mode: "lines",
//         name: 'Mean System Usage',
//         x: unpackData(parsedResponse, 'time'),
//         y: unpackData(parsedResponse, 'mean_usage_system'),
//         line: {color: '#7F7F7F'}
//       }
//       const data = [firstTrace, secondTrace];
//       const layout = {
//         title: 'Local CPU Usage',
//       };
//       return Plotly.newPlot('graphs-container', data, layout);
//     })
//     .catch( error => console.log(error) );
// }

const loadData = () => {
  fetch('/api/v1/main/0')
    .then( response => {
      if (response.status !== 200) {
        console.log(response);
      }
      return response;
    })
    .then(response => response.json())
    .then(parsedResponse => {
      const unpackData = (arr, key) => {
        return arr.map(obj => obj[key])
      }
      const unpackDate = (arr, key) => {
        return arr.map(obj => obj[key])
      }      
      const firstTrace = {
        type: 'scatter',
        name: 'Mean User Usage',
        x: unpackDate(parsedResponse, 'time'),
        y: unpackData(parsedResponse, 'g_data'),
        line: {color: '#17BECF'}
      }
      // const secondTrace = {
      //   type: "scatter",
      //   mode: "lines",
      //   name: 'Mean System Usage',
      //   x: unpackData(parsedResponse, 'time'),
      //   y: unpackData(parsedResponse, 'mean_usage_system'),
      //   line: {color: '#7F7F7F'}
      // }
      const data = [firstTrace];
      const layout = {
        title: 'G data for baseline',
        type: "date",
        xaxis: {
          autotick: true,
          ticks: 'outside',
          tick0: 1553357710369071872,
          dtick: 0.000000000000000000000025,
          tickcolor: '#000'
        },
        yaxis: {
          autotick: false,
          ticks: 'outside',
          tick0: 0,
          dtick: 0.25,
          ticklen: 8,
          tickwidth: 4,
          tickcolor: '#000'
        }
    }
      return Plotly.newPlot('graphs-container', data, layout);
    })
    .catch( error => console.log(error) );
}

const loadData1 = () => {
  fetch('/api/v1/main/1')
    .then( response => {
      if (response.status !== 200) {
        console.log(response);
      }
      return response;
    })
    .then(response => response.json())
    .then(parsedResponse => {
      const unpackData = (arr, key) => {
        return arr.map(obj => obj[key])
      }
      const firstTrace = {
        type: 'scatter',
        mode: 'lines',
        name: 'M',
        x: unpackData(parsedResponse, 'time'),
        y: unpackData(parsedResponse, 'g_data'),
        line: {color: '#17BECF'}
      }
      // const secondTrace = {
      //   type: "scatter",
      //   mode: "lines",
      //   name: 'Mean System Usage',
      //   x: unpackData(parsedResponse, 'time'),
      //   y: unpackData(parsedResponse, 'mean_usage_system'),
      //   line: {color: '#7F7F7F'}
      // }
      const data = [firstTrace];
      const layout = {
        title: 'G data for Inner fault',
         type: "date",
        xaxis: {
          autotick: true,
          ticks: 'outside',
          tick0: 1553357710369071872,
          dtick: 0.000000000000000000000025,
          tickcolor: '#000'
        },
        yaxis: {
          autotick: false,
          ticks: 'outside',
          tick0: 0,
          dtick: 0.25,
          ticklen: 8,
          tickwidth: 4,
          tickcolor: '#000'
        }
      };
      return Plotly.newPlot('graphs-container1', data, layout);
    })
    .catch( error => console.log(error) );
}

const loadData2 = () => {
  fetch('/api/v1/main/2')
    .then( response => {
      if (response.status !== 200) {
        console.log(response);
      }
      return response;
    })
    .then(response => response.json())
    .then(parsedResponse => {
      const unpackData = (arr, key) => {
        return arr.map(obj => obj[key])
      }
      const firstTrace = {
        type: 'scatter',
        mode: 'lines',
        name: 'M',
        x: unpackData(parsedResponse, 'time'),
        y: unpackData(parsedResponse, 'g_data'),
        line: {color: '#17BECF'}
      }
      // const secondTrace = {
      //   type: "scatter",
      //   mode: "lines",
      //   name: 'Mean System Usage',
      //   x: unpackData(parsedResponse, 'time'),
      //   y: unpackData(parsedResponse, 'mean_usage_system'),
      //   line: {color: '#7F7F7F'}
      // }
      const data = [firstTrace];
      const layout = {
        title: 'G data for Outer fault',
         type: "date",
        xaxis: {
          autotick: true,
          ticks: 'outside',
          tick0: 1553357710369071872,
          dtick: 0.000000000000000000000025,
          tickcolor: '#000'
        },
        yaxis: {
          autotick: false,
          ticks: 'outside',
          tick0: 0,
          dtick: 0.25,
          ticklen: 8,
          tickwidth: 4,
          tickcolor: '#000'
        }
      };
      return Plotly.newPlot('graphs-container1', data, layout);
    })
    .catch( error => console.log(error) );
}

$(window).on('load', loadData);
