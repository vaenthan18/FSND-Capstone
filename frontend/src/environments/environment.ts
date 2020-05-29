/* @TODO replace with your variables
 * ensure all variables on this page match your project
 */

export const environment = {
  production: false,
  apiServerUrl: 'https://vaenthan-casting-agency.herokuapp.com', // the running FLASK api server url
  auth0: {
    url: 'fsnd-vaenthan', // the auth0 domain prefix
    audience: 'casting', // the audience set for the auth0 app
    clientId: 'KZpq6rVEBOioAXspVX3z7919j1YxpVUN', // the client id generated for the auth0 app
    callbackURL: 'http://localhost:8100', // the base url of the running ionic application. 
  }
};
