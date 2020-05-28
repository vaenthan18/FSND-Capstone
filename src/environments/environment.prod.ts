export const environment = {
  production: true,
  apiServerUrl: 'http://127.0.0.1:5000',
  auth0: {
    url: 'fsnd-vaenthan', // the auth0 domain prefix
    audience: 'casting', // the audience set for the auth0 app
    clientId: 'KZpq6rVEBOioAXspVX3z7919j1YxpVUN', // the client id generated for the auth0 app
    callbackURL: 'http://localhost:8100', // the base url of the running ionic application. 
  }
};
