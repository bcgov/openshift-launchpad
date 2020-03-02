const path = require('path');

module.exports = {
  parser: 'babel-eslint',
  root: true,
  env: {
    node: true,
    browser: true,
    "jest/globals": true,
  },
  extends: [
    'eslint:recommended',
    'plugin:react/recommended',
    'airbnb-base',
  ],
  plugins: ['jest'],
  parserOptions: {},
  settings: {
    react: {
      version: 'detect',
    },
    'import/resolver': {
      alias: {
        map: [['@', path.join(__dirname, 'src')]],
      },
    },
  },
  rules: {
    'react/prop-types': 0,
  },
};
