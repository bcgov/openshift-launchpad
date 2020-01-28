const {success, fail} = require('./helpers');

// Tests that the / route responds successfully
module.exports = async browser => {
  const errors = [];
  const page = await browser.newPage();

  try {
    await page.goto('http://localhost:3000/');
    success();
  } catch (e) {
    fail();
    errors.push(e);
  }

  return errors;
};
