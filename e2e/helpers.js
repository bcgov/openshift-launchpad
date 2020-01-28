module.exports = {
  delay: timeout => {
    return new Promise((resolve, reject) => {
      setTimeout(resolve, timeout);
    });
  },
  success: () => {
    process.stdout.write('.');
  },
  fail: () => {
    process.stdout.write('F');
  },
  printResults: errors => {
    console.log('\n');
    if (errors.length > 0) {
      errors.forEach(msg => console.log(msg));
      const testGrammar = errors.length > 1 ? 'tests' : 'test';
      console.log(`\n${errors.length} ${testGrammar} failed`);
      process.exit(1);
    } else {
      console.log('All tests passed.');
    }
  },
};
