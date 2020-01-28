# React Frontend

This codebase is a minimal React starter with the following features:

- BrowserRouter client-side routing
- Webpack with Babel for code transformation and bundling
- Jest (with snapshot) testing

And the following development tooling:

- ESLint
- Prettier formatting
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
  conditional rendering based on incoming props. Sample Jest snapshot tests are
  provided for this component.
- AboutUs: A stateful component with an example API request integrated into the
  component state.
- NotFound: A stateless component used as the fall-through if no other routes
  are matched.

### Google Sign-in Support

#### Setup

Some quick POCs may require an integration with Google Sign-in. This support is
toggled off by default, but it can be easily enabled in the `App` component.

Past projets have been set up on [Google Developer
Console](https://console.developers.google.com/), so you may be able to reach
out for an existing `client_id`. This value is required to be set in the `.env`
as `GOOGLE_SIGNIN_CLIENT`.

If you are not able to acquire an existing `client_id` or would prefer to set
up your own, simply create a Google Developer Console project and configure an
"OAuth consent screen" to generate a valid `client_id`.

#### Components

The following components are included for Google Sign-in support:

- App: App is always included, but the version for Google Sign-in includes
  application-level state that tracks the user's authentication status.
- GoogleLoginButton: A class component that handles the sign-in/out actions. It
  accepts callbacks as props to update the application-level state in App.
- Login: A stateless component to be rendered when an unauthenticated user
  attempts to view a private route.

When Google Sign-in is not needed, please remove the `GoogleLoginButton` and
`Login` components. You should also prefer the stateless version of the `App`
component.

#### Routing

Public and private routes have been set up to be as simple as possible. By
leveraging the application state, private routes are conditionally rendered. To
add more public or private routes, simply add more routes to their respective
`Switch`es in `Routes.js`. New routes are automatically included in `App`.

### Linting and Formatting

This project has been pre-configured with Prettier and ESLint to work with the
provided tooling/environments. A typical IDE will observe the configuration
files automatically.

If you run into difficulties with IDE-based formatting, you can use the
provided npm script to apply formatting to the codebase.

```
$ npm run format
```

A similar script exists for linting

```
$ npm run lint
```

#### IDE Configuration for Formatting

This codebase uses Prettier for formatting. This means that the IDE being used
should have any other formatters (ex. Beautify) disabled. If the IDE provides
formatting on-save, it is beneficial to enable that setting.

If your IDE is not observing the configuration file(s) correctly, it is
advisable to disable all auto-formatting to avoid inconsistencies.

## License

Code released under the [Apache License, Version 2.0](LICENSE).
