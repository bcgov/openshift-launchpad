const puppeteer = require('puppeteer');
const {printResults} = require('./helpers');
const homeTest = require('./homeTest');
const apiTest = require('./apiTest');

const tests = async () => {
  const browser = await puppeteer.launch();

  const homeErrors = await homeTest(browser);
  const apiErrors = await apiTest(browser);

  return {browser, errors: [...homeErrors, ...apiErrors]};
};

tests().then(({browser, errors}) => {
  printResults(errors);
  browser.close();
});
