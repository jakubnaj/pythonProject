import { Component, OnInit, Input } from "@angular/core";
import { ArticleDetailsService } from "../../services/article-details.service";
import { NgForm } from "@angular/forms";
import { Comment } from "../../models/comment";
import { AuthService } from "../../../shared/services/auth/auth.service";

@Component({
  selector: "app-comments",
  templateUrl: "./comments.component.html",
  styleUrls: ["./comments.component.scss"]
})
export class CommentsComponent implements OnInit {
  @Input() adviceID: Number;
  error: string;
  comments: Comment[];
  username: String;
  constructor(
    private articleDetailsService: ArticleDetailsService,
    private authService: AuthService
  ) {}

  ngOnInit() {
    this.username = localStorage.getItem("username");
    this.authService.activeName.subscribe(active => (this.username = active));
    this.getComments();
  }
  getComments() {
    this.articleDetailsService.getComments(this.adviceID).subscribe(
      data => {
        this.comments = data;
      },
      error => console.error(error)
    );
  }
  addComment(form: NgForm) {
    const comment: Comment = {
      adviceID: this.adviceID,
      authorName: this.username,
      content: form.value.commentBody,
      likesQuantity: 0
    };
    this.articleDetailsService.createComment(comment).subscribe(
      data => {
        this.getComments();
      },
      error => {
        this.error = error.message;
      }
    );
  }
}
