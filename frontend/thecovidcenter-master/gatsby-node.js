const path = require("path")

exports.onCreatePage = async ({ page, actions }) => {
  const { createPage } = actions

  if (page.path.match(/^\/country/)) {
    createPage({
      path: "/country",
      matchPath: "/country/*",
      component: path.resolve("src/pages/country.js"),
      context: {},
    })
  }

  if (page.path.match(/^\/states/)) {
    createPage({
      path: "/states",
      matchPath: "/states/*",
      component: path.resolve("src/pages/states.js"),
      context: {},
    })
  }

  if (page.path.match(/^\/singlenews/)) {
    createPage({
      path: "/singlenews",
      matchPath: "/singlenews/*",
      component: path.resolve("src/pages/singlenews.js"),
      context: {},
    })
  }

  if (page.path.match(/^\/singleblog/)) {
    createPage({
      path: "/singleblog",
      matchPath: "/singleblog/*",
      component: path.resolve("src/pages/singleblog.js"),
      context: {},
    })
  }
}

exports.onCreateWebpackConfig = ({ stage, loaders, actions }) => {
  if (stage === "build-html") {
    actions.setWebpackConfig({
      module: {
        rules: [
          {
            test: /\@amcharts/,
            use: loaders.null(),
          },
          {
            test: /leaflet/,
            use: loaders.null(),
          },
        ],
      },
    })
  }
}
