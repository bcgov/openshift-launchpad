# React Frontend

This codebase is a minimal React starter with the following features:

- BrowserRouter client-side routing
- Webpack with Babel for code transformation and bundling

And the following development tooling:

- ESLint
- SASS support
- Webpack Dev Server with hot module replacement

## Getting Started

Start a local development build of the project

```
$ npm run serve
```

The project can, instead, be run with Docker.

```
$ docker build . -t minimal-react
$ docker run -d -p 3000:3000 minimal-react
```

Running with Docker should always produce a Production-ready build. This is not
useful for development. However, as this repo is being used as a submodule in
fullstack projects, the success of running with Docker must be retained.

## Development

### Examples

The `index.html` file is used as a template for the built `index.html` that
will be created in `/dist`. If you need to add third-party scripts to your
build, you may choose to add them here. Note that the output bundle for your
build will be injected into the template. If you modify the template directly,
be careful not to create a conflict with the injected bundle.

Routing is controlled by a Switch component in `Routes.js`.

The following sample components are provided:

- Home: The landing-page component. It includes a Link to `/about-us` as an
  example of routing to another page/component. It also provides an example of
  conditional rendering based on incoming props.
- AboutUs: A stateful component with an example API request integrated into the
  component state.
- NotFound: A stateless component used as the fall-through if no other routes
  are matched.

### Linting

This project has been pre-configured with ESLint to work with the
provided tooling/environments.

```
$ npm run lint
```

## License

Code released under the [Apache License, Version 2.0](LICENSE).