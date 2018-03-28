import { NgModule } from "@angular/core";
import { CommonModule } from "@angular/common";
import { RouterModule, Routes } from "@angular/router";
import { WallContainerComponent } from "./wall/components/wall-container.component";
import { ArticleDetailsComponent } from "./article-details/article-details.component";
import { ArticleDetailsModule } from "./article-details/article-details.module";
import { LoginComponent } from "./account/components/login/login.component";
import { RegisterComponent } from "./account/components/register/register.component";
import { ForgotPasswordComponent } from "./account/components/forgot-password/forgot-password.component";
import { ResetPasswordComponent } from "./account/components/reset-password/reset-password.component";
import { AddArticleComponent } from "./wall/components/add-article/add-article.component";

const appRoutes: Routes = [
  { path: "category/:categoryName", component: WallContainerComponent },
  { path: "", component: WallContainerComponent, pathMatch: "full" },
  { path: "article/:articleID", component: ArticleDetailsComponent },
  { path: "login", component: LoginComponent },
  { path: "register", component: RegisterComponent },
  { path: "forgot-password", component: ForgotPasswordComponent },
  { path: "reset-password", component: ResetPasswordComponent },
  { path: "add-article", component: AddArticleComponent },
];

@NgModule({
  imports: [
    RouterModule.forRoot(appRoutes),
    CommonModule,
    ArticleDetailsModule
  ],
  declarations: []
})
export class RoutingModule {}
