// The file contents for the current environment will overwrite these during build.
// The build system defaults to the dev environment which uses `environment.ts`, but if you do
// `ng build --env=prod` then `environment.prod.ts` will be used instead.
// The list of which env maps to which file can be found in `.angular-cli.json`.

export const environment = {
  production: false,
  endpoints: {
    advice: "http://localhost:5000/api/v1/advice",
    createUser: "http://localhost:5000/api/v1/user",
    getArticle: "http://localhost:5000/api/v1/advice/" ,
    getAdviceComments: "http://localhost:5000/api/v1/adviceComments/",
    getCategories: "http://localhost:5000/api/v1/category",
    login: "http://localhost:5000/api/v1/user/auth",
    comment: "http://localhost:5000/api/v1/comment"
  }
};
