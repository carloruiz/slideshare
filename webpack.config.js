const HtmlWebPackPlugin = require("html-webpack-plugin");
const path = require('path');
const webpack = require('webpack');

const babelOptions = {
    presets: ["@babel/preset-env", "@babel/preset-react"],
    plugins: [
      "@babel/plugin-proposal-export-default-from", 
      ["@babel/plugin-proposal-decorators", {"legacy": true}],
      "@babel/plugin-proposal-class-properties",
      "@babel/plugin-syntax-dynamic-import"
    ]
  }


module.exports = {
  mode: 'development',
  entry: {
    'home': './src/components/home.jsx',
    'login': './src/components/login.jsx',
    'test': './src/components/test.jsx'
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
        test: /\.js$/,
        exclude: /node_modules\/(?!(formol)\/).*/,
        loaders: 'babel-loader',
        options: babelOptions 
      },
      {
        test:  /\.jsx$/,
        exclude: /node_modules\/(?!(formol)\/).*/,
        loaders: 'babel-loader',
        options: babelOptions
      },
      {
        test: /\.css$/,
        loaders: 'style-loader?sourceMap', 
        options: {
          sourceMap: true
        }
      },
      {
        test: /\.css$/,
        loaders: 'css-loader',
        options: {
          importLoaders: true,
          modules: true,
          localIdentName: '[path]___[name]__[local]___[hash:base64:5]'
        }
      }
    ],
  },
  resolve: {
    extensions: ['.js', '.jsx']
  }
};
