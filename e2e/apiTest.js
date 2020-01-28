const {success, fail, delay} = require('./helpers');

// Tests that the API is successfully integrated with the UI
module.exports = async browser => {
  const errors = [];
  const page = await browser.newPage();
  await page.goto('http://localhost:3000/about-us');
  const responseDataElement = await page.$('p');

  const attemptTest = async attemptsRemaining => {
    try {
      // Setup test data
      const responseData = await page.evaluate(
        element => element.textContent,
        responseDataElement,
      );
      const expected = 'hello world';
      const actual = responseData.toLowerCase();

      // Test assertion
      if (actual.includes(expected)) {
        success();
      } else {
        throw new Error(
          `Response data expected to include "${expected}" but was: "${actual}"`,
        );
      }
    } catch (e) {
      // Handle error on final attempt
      if (attemptsRemaining <= 0) {
        fail();
        errors.push(e);

      // Wait and then retry
      } else {
        await delay(1000);
        return attemptTest(attemptsRemaining - 1);
      }
    }
  };

  await attemptTest(5);

  return errors;
};
