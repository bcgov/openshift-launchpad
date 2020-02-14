module.exports = {
  testURL: 'http://localhost/',
  testEnvironment: 'jsdom',
  setupFiles: ['<rootDir>/jest.setup.js'],
  moduleNameMapper: {
    '\\.(jpg|jpeg|png|gif|eot|otf|webp|svg|ttf|woff|woff2|mp4|webm|wav|mp3|m4a|aac|oga)$': 'jest-transform-stub',
    '\\.(css|less|scss|sass)$': 'identity-obj-proxy',
    '\\@/(.*)$': '<rootDir>/src/$1',
  },
};
