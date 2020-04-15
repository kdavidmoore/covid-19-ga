#!/usr/bin/env node

const axios = require('axios');
const moment = require('moment');
const fs = require('fs');
const { parseAsync } = require('json2csv');
const BASE_URL = 'https://covidtracking.com/api/states/daily?state=GA&date=';

async function getData() {
  try {
    const now = moment();
    let data = [];
    let formattedDate = now.format('YYYYMMDD');
    while (formattedDate !== '20200330') {
      console.log(formattedDate);

      const results = await axios.get(`${BASE_URL}${formattedDate}`)
        .catch((err) => {
          console.log(err);
          return null;
        });

      if (results) {
        const elem = results.data;
        if (elem && !Array.isArray(elem) && !elem.error) {
          data = data.concat([elem]);
        } else if (Array.isArray(elem) && elem.length === 0) {
          console.log('no results:', elem);
        } else {
          console.log('invalid result format:', elem);
        }
      }

      now.subtract(1, 'day');
      formattedDate = now.format('YYYYMMDD');
    }

    return data;
  } catch (err) {
    console.log(err);
    return err;
  }
}

function calculateNewDailyCases(data) {
  for (let i = 0, len = data.length; i < len; i += 1) {
    const elem = data[i];
    const prev = data[i + 1];
    if (prev && prev.positive !== null) {
      const diff = elem.positive - prev.positive;
      elem.newCases = diff;
    } else {
      elem.newCases = null;
    }
  }
}

async function writeCsv(data) {
  try {
    const fields = Object.keys(data[0]);
    const opts = { fields };
    const csvFile = await parseAsync(data, opts);
    return fs.writeFileSync('covid-19-ga-data.csv', csvFile, 'utf8');
  } catch (err) {
    throw err;
  }
}

async function main() {
  try {
    const data = await getData();
    // calculateNewDailyCases(data);
    console.log(JSON.stringify(data));
    return writeCsv(data);
  } catch (err) {
    console.log(err);
    return null;
  }
}

main();
