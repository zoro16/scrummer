const path = require('path')
const webpack = require('webpack')
const BundleTracker = require('webpack-bundle-tracker')
const isProd = process.env.NODE_ENV === 'production';

const config = {
    context: __dirname,
    entry: {
      App: './assets/js/App.jsx',
    },
    output: {
        path: path.resolve('./assets/bundles/'),
        filename: isProd ? '[name]-[hash].js' : '[name].js',
    },
    plugins: [],
    module: {
        loaders: []
    },
    resolve: {
        modules: ['node_modules', 'bower_components'],
        extensions: ['.js', '.jsx']
    },

};

if (isProd) {
    config.output.path = require('path').resolve('./assets/bundles/')

    config.plugins = config.plugins.concat([
        new BundleTracker({filename: './webpack-stats.json'}),
        // removes a lot of debugging code in React
        new webpack.DefinePlugin({
            'process.env': {
                'NODE_ENV': process.env.NODE_ENV,
            }}),

        new webpack.optimize.UglifyJsPlugin({
            compressor: {
                warnings: false
            }
        })
    ])

    config.module.loaders.push(
        { test: /\.jsx?$/, exclude: /node_modules/, loader: 'babel-loader' }
    )

} else {
    var ip = 'localhost'
    config.output.publicPath = 'http://' + ip + ':3000' + '/assets/bundles/'
    config.plugins = config.plugins.concat([
      new webpack.HotModuleReplacementPlugin(),
      new webpack.NoEmitOnErrorsPlugin(),
      new BundleTracker({filename: './webpack-stats.json'}),
    ])
    config.module.loaders.push(
      { test: /\.jsx?$/, exclude: /node_modules/, loaders: ['react-hot-loader', 'babel-loader'] }
    )
    config.cache = true;
    config.devtool = 'eval'; //or cheap-module-eval-source-map
    config.plugins.push(
        new webpack.DefinePlugin({
            '__DEV__': true
        })
    );
    config.devServer = {
        contentBase: __dirname,
        host: ip,
        port: Number('3000'),
        inline: true,
    };

}



module.exports = config
