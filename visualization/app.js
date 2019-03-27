const Influx = require('influx');
const express = require('express');
const path = require('path');
const os = require('os');
const bodyParser = require('body-parser');
const app = express();
const influx = new Influx.InfluxDB('http://localhost:8086/complete_data');

app.use(bodyParser.json());
app.use(bodyParser.urlencoded({
  extended: true
}));
app.use(express.static(path.join(__dirname, 'public')));
app.set('port', 3000);

influx.getMeasurements()
  .then(names => console.log('My measurement names are: ' + names.join(', ')))
  .then(() => {
    app.listen(app.get('port'), () => {
      console.log(`Listening on ${app.get('port')}.`);
    });
  })
  .catch(error => console.log({ error }));

// app.get('/api/v1/usage', (request, response) => {
//   influx.query(`
//     select gs as "g data",
//     mean("usage_system") as "mean_usage_system" from cpu
//     where time > now() - 1h and
//     host = ${Influx.escape.stringLit(os.hostname())}
//     group by time(10s)
//     order by time desc
//     limit 200
//     `)
//     .then(result => response.status(200).json(result))
//     .catch(error => response.status(500).json({ error }));
// });



app.get('/api/v1/main/0', (request, response) => {
  influx.query(`
    select gs, label from iot_fault_data
    order by time desc
    limit 20000 
    `)
    .then(result => {
      // console.log(result[0])
      dataR = []
      for(i=0; i <result.length; i++) {
          data = {};

          data['time'] = result[i]['time'].getNanoTime();
          data['g_data'] = result[i]['gs'];
          data['label'] = result[i]['label']
          dataR.push(data)
        
      }
 
      response.status(200).json(dataR)
    })
    .catch(error => 
      {
        console.log(error)
        response.status(500).json({ error })
    });
});

app.get('/api/v1/main/1', (request, response) => {
  influx.query(`
    select gs, label from iot_fault_data
    order by time desc
    limit 20000
    `)
    .then(result => {
      // console.log(result[0])
      dataR = []
      for(i=0; i <result.length; i++) {
        if(result[i]['label'] == 1) {
          data = {};

          data['time'] = result[i]['time'].getNanoTime();
          data['g_data'] = result[i]['g_data'];
          dataR.push(data)
        }
      }
 
      response.status(200).json(dataR)
    })
    .catch(error => 
      {
        console.log(error)
        response.status(500).json({ error })
    });
});

app.get('/api/v1/main/2', (request, response) => {
  influx.query(`
    select gs as "g_data, label" from iot_fault_data
    limit 20000 
    `)
    .then(result => {
      // console.log(result[0])
      dataR = []
      for(i=0; i <result.length; i++) {
        if(result[i]['label'] == 2) {
          data = {};

          data['time'] = result[i]['time'].getNanoTime();
          data['g_data'] = result[i]['g_data'];
          dataR.push(data)
        }
      }

      response.status(200).json(dataR)
    })
    .catch(error => 
      {
        console.log(error)
        response.status(500).json({ error })
    });
});

app.get('/api/v1/fault/0', (request, response) => {
  influx.query(`
    select gs as "g_data, label" from iot_fault_data_result
    where label=0
    limit 20000 
    `)
    .then(result => {
      // console.log(result[0])
      dataR = []
      for(i=0; i <result.length; i++) {
        if(result[i]['label'] == 0) {
          data = {};

          data['time'] = result[i]['time'].getNanoTime();
          data['g_data'] = result[i]['g_data'];
          dataR.push(data)
        }
      }
      console.log(dataR)
      response.status(200).json(dataR)
    })
    .catch(error => 
      {
        console.log(error)
        response.status(500).json({ error })
    });
});

app.get('/api/v1/fault/1', (request, response) => {
  influx.query(`
    select gs as "g_data, label" from iot_fault_data_result
    limit 20000 
    `)
    .then(result => {
      // console.log(result[0])
      dataR = []
      for(i=0; i <result.length; i++) {
        if(result[i]['label'] == 1) {
          data = {};

          data['time'] = result[i]['time'].getNanoTime();
          data['g_data'] = result[i]['g_data'];
          dataR.push(data)
        }
      }
      console.log(dataR)
      response.status(200).json(dataR)
    })
    .catch(error => 
      {
        console.log(error)
        response.status(500).json({ error })
    });
});

app.get('/api/v1/fault/2', (request, response) => {
  influx.query(`
    select gs as "g_data, label" from iot_fault_data_result
    limit 20000 
    `)
    .then(result => {
      // console.log(result[0])
      dataR = []
      for(i=0; i <result.length; i++) {
        if(result[i]['label'] == 2) {
          data = {};

          data['time'] = result[i]['time'].getNanoTime();
          data['g_data'] = result[i]['g_data'];
          dataR.push(data)
        }
      }
      console.log(dataR)
      response.status(200).json(dataR)
    })
    .catch(error => 
      {
        console.log(error)
        response.status(500).json({ error })
    });
});