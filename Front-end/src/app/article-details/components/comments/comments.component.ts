import { Component, OnInit, Input } from "@angular/core";
import { ArticleDetailsService } from "../../services/article-details.service";

@Component({
  selector: "app-comments",
  templateUrl: "./comments.component.html",
  styleUrls: ["./comments.component.scss"]
})
export class CommentsComponent implements OnInit {
  @Input() adviceID: Number;
  comments: Array<Comment>;
  constructor(private articleDetailsService: ArticleDetailsService) {}

  ngOnInit() {
    this.articleDetailsService
      .getComments(this.adviceID)
      .subscribe(data => (this.comments = data), error => console.error(error));
  }
}
