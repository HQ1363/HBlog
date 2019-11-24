'use strict'
const path = require('path')

module.exports = {
  context: path.resolve(__dirname, './'),
  resolve: {
    extensions: ['.js', '.vue', '.json'],
    alias: {
      '@': path.resolve('src'),
      '@assets': path.resolve(__dirname, 'src/assets'),
      '@views': path.resolve(__dirname, 'src/views'),
      '@comp': path.resolve(__dirname, 'src/components'),
      '@api': path.resolve(__dirname, 'src/api'),
      '@plugins': path.resolve(__dirname, 'src/plugins'),
      '@utils': path.resolve(__dirname, 'src/utils')
    }
  }
}
