import { Component, OnInit } from "@angular/core";
import { NavigationService } from "../../services/navigation.service";
import { Category } from "../../models/category";

@Component({
  selector: "app-header-home",
  templateUrl: "./header-home.component.html",
  styleUrls: ["./header-home.component.scss"]
})
export class HeaderHomeComponent implements OnInit {
  categories: Category[];
  constructor(private navigationService: NavigationService) {}

  ngOnInit() {
    this.navigationService
      .getCategories()
      .subscribe(
        data => (this.categories = data),
        error => console.error(error)
      );
  }
}
