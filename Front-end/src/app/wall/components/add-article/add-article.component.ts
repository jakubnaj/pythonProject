import { Component, OnInit } from "@angular/core";
import { CategoryService } from "../../../shared/services/category/category.service";
import { Category } from "../../../navigation/models/category";
import { NgForm } from "@angular/forms";
import { Advice } from "../../../shared/models/advice";
import { ArticleService } from "../../services/article.service";
import { Router } from "@angular/router";

@Component({
  selector: "app-add-article",
  templateUrl: "./add-article.component.html",
  styleUrls: ["./add-article.component.scss"]
})
export class AddArticleComponent implements OnInit {
  error: String;
  categories: Category[];
  constructor(
    private categoryService: CategoryService,
    private articleService: ArticleService,
    private router: Router
  ) {}

  ngOnInit() {
    this.categoryService
      .getCategories()
      .subscribe(
        data => (this.categories = data),
        error => console.error(error)
      );
  }

  add(form: NgForm) {
    if (
      !(localStorage.getItem("username") && localStorage.getItem("password"))
    ) {
      this.router.navigate(["/login"]);
    }
    let advice: any = {};
    let tempObj = form.value;
    advice.title = tempObj.adTitle;
    advice.shortDescription = tempObj.shortDesc;
    advice.body = tempObj.body;
    advice.categoryName = tempObj.category;

    advice.authorName = localStorage.getItem("username");

    this.articleService.create(advice).subscribe(data => {
      this.router.navigate([""]), error => (this.error = error.message);
    });
  }
}
