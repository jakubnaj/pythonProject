import { NgModule } from "@angular/core";
import { CommonModule } from "@angular/common";
import { HttpClientModule } from "@angular/common/http";
import { AuthService } from "./services/auth/auth.service";
import { CategoryService } from "./services/category/category.service";

@NgModule({
  imports: [CommonModule, HttpClientModule],
  providers: [AuthService,CategoryService],
  declarations: []
})
export class SharedModule {}
