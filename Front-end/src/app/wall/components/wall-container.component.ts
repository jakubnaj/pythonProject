import { Component, OnInit, OnChanges } from "@angular/core";
import { ArticleService } from "../services/article.service";
import { ActivatedRoute, Router } from "@angular/router";
import { Advice } from "../../shared/models/advice";
import { WallCommunicationService } from "../services/wall-communication.service";

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
    private wallCommunicationService: WallCommunicationService,
    private article: ArticleService
  ) {}
  ngOnInit() {
    this.article.getArticle().subscribe(data => {
      this.originalAdvices = data.sort((x, y) => {
        return Number(y.createDate) - Number(x.createDate);
      });
      this.advices = this.originalAdvices;
    });
    this.wallCommunicationService.activeName.subscribe(data => {
      if (data === "wall") {
        console.log('pipa');
        this.advices = this.originalAdvices;
      } else if (data === "top") {
        let temp = Object.create(this.originalAdvices);
        this.advices = this.sort(temp);
      } else {
        this.advices = this.filter(this.originalAdvices, data);
      }
    });
  }
  filter(advices: Advice[], name: string) {
    return this.article.filterByCategory(advices, name);
  }
  sort(advices: Advice[]) {
    return this.article.sortBySeen(advices);
  }
}
