const path = require('path');
const webpack = require('webpack');
const HtmlWebpackPlugin = require('html-webpack-plugin');
const { CleanWebpackPlugin } = require('clean-webpack-plugin');

const HOST = process.env.HOST || '0.0.0.0';
const PORT = process.env.PORT || 3000;

const prodConfig = {
  name: 'prod',
  entry: './src/index.js',
  mode: 'production',
  module: {
    rules: [
      {
        test: /\.(js|jsx)$/,
        exclude: /node_modules/,
        use: ['babel-loader'],
      },
      {
        test: /\.s[ac]ss$/i,
        use: ['style-loader', 'css-loader', 'sass-loader'],
      },
    ],
  },
  resolve: {
    extensions: ['*', '.js', '.jsx'],
    alias: {
      '@': path.join(__dirname, 'src'),
    },
  },
  output: {
    path: path.join(__dirname, 'dist'),
    publicPath: './',
    filename: 'bundle.js',
  },
  plugins: [
    new CleanWebpackPlugin(),
    new HtmlWebpackPlugin({
      title: 'Basic React App',
      template: './src/index.html',
    }),
    new webpack.EnvironmentPlugin({ API_URL: 'http://localhost:5000/api' }),
  ],
};
const devConfig = {
  ...prodConfig,
  name: 'dev',
  mode: 'development',
  devServer: {
    contentBase: './dist',
    hot: true,
    historyApiFallback: true,
    writeToDisk: true,
    host: HOST,
    port: PORT,
  },
};

module.exports = [prodConfig, devConfig];
