const HtmlWebPackPlugin = require("html-webpack-plugin");
const path = require('path');
const webpack = require('webpack');


module.exports = {
  mode: 'development',
  entry: {
    'home': './src/components/home.jsx',
    'login': './src/components/login.jsx'
  },
  output: {
    path: path.resolve(__dirname, 'logic/static/logic/'),
    filename: '[name].js'
  },
  devtool: 'inline-source-map',
  devServer: {
    contentBase: path.resolve(__dirname, 'logic/static/logic/'),
    hot: true
  },
  plugins: [
    new webpack.HotModuleReplacementPlugin()
  ],
  module: {
    rules: [
      {
        test: /\.jsx$/,
        exclude: /node_modules/,
        use: {
          loader: "babel-loader"
        }
      },
      {
        test: /\.css$/,
        loaders: [
          'style-loader?sourceMap',
          'css-loader?modules&importLoaders=1&localIdentName=[path]___[name]__[local]___[hash:base64:5]'
        ]
      },
    ]
  },
};
