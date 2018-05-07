import { Component, OnInit, Input } from "@angular/core";
import { AuthService } from "../../../shared/services/auth/auth.service";
import { ArticleDetailsService } from "../../services/article-details.service";
import { Comment } from "../../models/comment";
import { Tag } from "../../../account/models/tag";

@Component({
  selector: "app-statistics",
  templateUrl: "./statistics.component.html",
  styleUrls: ["./statistics.component.scss"]
})
export class StatisticsComponent implements OnInit {
  @Input() tags: string;
  @Input() adviceID: number;
  error: string;
  comments: Comment[];
  username: String;
  tagArray: string[];
  statistics: Array<Tag> = [];

  constructor(
    private articleDetailsService: ArticleDetailsService,
    private authService: AuthService
  ) {}

  ngOnInit() {
    this.username = localStorage.getItem("username");
    this.authService.activeName.subscribe(active => (this.username = active));
    this.getTagsArray();
    this.getComments();
  }
  getComments() {
    this.articleDetailsService.getComments(this.adviceID).subscribe(
      data => {
        this.comments = data;
        this.getStatistics();
        this.sortStatistics();
      },
      error => console.error(error)
    );
  }
  getTagsArray() {
    if (this.tags) {
      this.tagArray = this.tags.split(",");
    }
  }
  getStatistics() {
    for (let comment of this.comments) {
      for (let tag of this.tagArray) {
        if (comment.content.includes(tag)) {
          if (this.statistics.length === 0) {
            if (comment.likesQuantity > 0) {
              this.statistics.push({
                name: tag,
                likesQuantity: Math.abs(Number(comment.likesQuantity)),
                unLikesQuantity: 0
              });
            } else if (comment.likesQuantity < 0) {
              this.statistics.push({
                name: tag,
                likesQuantity: 0,
                unLikesQuantity: Math.abs(Number(comment.likesQuantity))
              });
            }
          } else {
            if (this.tagExists(tag)) {
              for (let stat of this.statistics) {
                if (stat.name === tag) {
                  if (comment.likesQuantity > 0) {
                    stat.likesQuantity += Math.abs(Number(comment.likesQuantity));
                  } else if (comment.likesQuantity < 0) {
                    stat.unLikesQuantity += Math.abs(Number(comment.likesQuantity));
                  }
                }
              }
            } else {
              if (comment.likesQuantity > 0) {
                this.statistics.push({
                  name: tag,
                  likesQuantity: Math.abs(Number(comment.likesQuantity)),
                  unLikesQuantity: 0
                });
              }
              if (comment.likesQuantity < 0) {
                this.statistics.push({
                  name: tag,
                  likesQuantity: 0,
                  unLikesQuantity: Math.abs(Number(comment.likesQuantity))
                });
              }
            }
          }
        }
      }
    }
    for (let tag of this.tagArray) {
      if (!this.tagExists(tag)) {
        this.statistics.push({
          name: tag,
          likesQuantity: 0,
          unLikesQuantity: 0
        });
      }
    }
  }
  tagExists(tagName) {
    return this.statistics.some(el => {
      return el.name === tagName;
    });
  }
  sortStatistics(){
    this.statistics = this.statistics.sort((x,y)=>{
      return ((y.likesQuantity/(y.likesQuantity+y.unLikesQuantity))*100) - ((x.likesQuantity/(x.likesQuantity+x.unLikesQuantity))*100);
    })
  }
}
