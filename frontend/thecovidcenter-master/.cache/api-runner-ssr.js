var plugins = [{
      plugin: require('/home/arslan/Documents/personel/scrature/Smeedies-Log-master/covid-19/frontend/thecovidcenter-master/node_modules/gatsby-plugin-react-helmet/gatsby-ssr'),
      options: {"plugins":[]},
    },{
      plugin: require('/home/arslan/Documents/personel/scrature/Smeedies-Log-master/covid-19/frontend/thecovidcenter-master/node_modules/gatsby-plugin-fontawesome-css/gatsby-ssr'),
      options: {"plugins":[]},
    },{
      plugin: require('/home/arslan/Documents/personel/scrature/Smeedies-Log-master/covid-19/frontend/thecovidcenter-master/node_modules/gatsby-plugin-manifest/gatsby-ssr'),
      options: {"plugins":[],"name":"gatsby-starter-default","short_name":"starter","start_url":"/","background_color":"#663399","theme_color":"#663399","display":"minimal-ui","icon":"src/images/gatsby-icon.png","cache_busting_mode":"query","include_favicon":true,"legacy":true,"theme_color_in_head":true,"cacheDigest":"4a9773549091c227cd2eb82ccd9c5e3a"},
    },{
      plugin: require('/home/arslan/Documents/personel/scrature/Smeedies-Log-master/covid-19/frontend/thecovidcenter-master/node_modules/gatsby-plugin-google-fonts/gatsby-ssr'),
      options: {"plugins":[],"fonts":["Montserrat:300,400,500,700,800,900"],"display":"swap"},
    },{
      plugin: require('/home/arslan/Documents/personel/scrature/Smeedies-Log-master/covid-19/frontend/thecovidcenter-master/node_modules/gatsby-plugin-load-script/gatsby-ssr'),
      options: {"plugins":[],"src":"https://unpkg.com/leaflet@1.6.0/dist/leaflet.js"},
    }]
// During bootstrap, we write requires at top of this file which looks like:
// var plugins = [
//   {
//     plugin: require("/path/to/plugin1/gatsby-ssr.js"),
//     options: { ... },
//   },
//   {
//     plugin: require("/path/to/plugin2/gatsby-ssr.js"),
//     options: { ... },
//   },
// ]

const apis = require(`./api-ssr-docs`)

// Run the specified API in any plugins that have implemented it
module.exports = (api, args, defaultReturn, argTransform) => {
  if (!apis[api]) {
    console.log(`This API doesn't exist`, api)
  }

  // Run each plugin in series.
  // eslint-disable-next-line no-undef
  let results = plugins.map(plugin => {
    if (!plugin.plugin[api]) {
      return undefined
    }
    const result = plugin.plugin[api](args, plugin.options)
    if (result && argTransform) {
      args = argTransform({ args, result })
    }
    return result
  })

  // Filter out undefined results.
  results = results.filter(result => typeof result !== `undefined`)

  if (results.length > 0) {
    return results
  } else {
    return [defaultReturn]
  }
}
