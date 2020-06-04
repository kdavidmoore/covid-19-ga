#!/usr/bin/env node

const axios = require('axios');
const fs = require('fs');
const { parseAsync } = require('json2csv');
const BASE_URL = 'https://covidtracking.com/api/v1/states/ga/daily.json';

async function getData() {
  try {
    const results = await axios.get(BASE_URL);
    return results.data;
  } catch (err) {
    console.log(err);
    return err;
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
    console.log(JSON.stringify(data));
    return writeCsv(data);
  } catch (err) {
    console.log(err);
    return null;
  }
}

main();
