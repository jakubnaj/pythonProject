import { Component, OnInit, OnChanges } from "@angular/core";
import { ArticleService } from "../services/article.service";
import { ActivatedRoute, Router } from "@angular/router";
import { Advice } from "../../shared/models/advice";

@Component({
  selector: "app-wall-container",
  templateUrl: "./wall-container.component.html",
  styleUrls: ["./wall-container.component.scss"]
})
export class WallContainerComponent implements OnInit {
  originalAdvices: Advice[];
  advices: Advice[];
  categoryName: String;
  constructor(
    private route: ActivatedRoute,
    private article: ArticleService,
    private activatedRoute: ActivatedRoute
  ) {}
  ngOnInit() {
    this.article.getArticle().subscribe(data => {
      this.originalAdvices = data;
      this.advices = data;
    });
    this.route.paramMap.subscribe(params => {
      if (params.get("categoryName") && this.originalAdvices) {
        this.advices = this.article.filterByCategory(
          this.originalAdvices,
          params.get("categoryName")
        );
      }
    });
  }
}
