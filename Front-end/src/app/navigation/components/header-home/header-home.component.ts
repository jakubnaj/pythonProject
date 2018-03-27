import { Component, OnInit } from "@angular/core";
import { NavigationService } from "../../services/navigation.service";
import { Category } from "../../models/category";
import { CategoryService } from "../../../shared/services/category/category.service";
import { AuthService } from "../../../shared/services/auth/auth.service";

@Component({
  selector: "app-header-home",
  templateUrl: "./header-home.component.html",
  styleUrls: ["./header-home.component.scss"]
})
export class HeaderHomeComponent implements OnInit {
  categories: Category[];
  username: String;
  constructor(
    private categoryService: CategoryService,
    private authService: AuthService
  ) {}

  ngOnInit() {
    this.username = localStorage.getItem("username");
    this.authService.activeName.subscribe(active => this.username = active);
    this.categoryService
      .getCategories()
      .subscribe(
        data => (this.categories = data),
        error => console.error(error)
      );
  }
  logout() {
    this.authService.logout();
  }
}
