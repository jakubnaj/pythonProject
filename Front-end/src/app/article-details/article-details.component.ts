import { Component, OnInit } from "@angular/core";
import { ActivatedRoute } from "@angular/router";
import { ArticleDetailsService } from "./services/article-details.service";
import { Advice } from "../shared/models/advice";

@Component({
  selector: "app-article-details",
  templateUrl: "./article-details.component.html",
  styleUrls: ["./article-details.component.scss"]
})
export class ArticleDetailsComponent implements OnInit {
  article: Advice;
  articleID: Number;
  constructor(
    private route: ActivatedRoute,
    private articleDetailsService: ArticleDetailsService
  ) {
    this.route.paramMap.subscribe(params => {
      this.articleID = Number(params.get("articleID"));
    });
  }

  ngOnInit() {
    this.articleDetailsService.getArticle(this.articleID).subscribe(
      data => {
        this.article = data[0];
      },
      error => {
        console.log(error);
      }
    );
  }
}
