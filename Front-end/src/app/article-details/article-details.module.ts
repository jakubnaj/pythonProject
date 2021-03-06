import { NgModule } from "@angular/core";
import { FormsModule } from '@angular/forms';
import { CommonModule } from "@angular/common";
import { ArticleDetailsComponent } from "./article-details.component";
import { CommentsComponent } from "./components/comments/comments.component";
import { AdviceComponent } from "./components/advice/advice.component";
import { ArticleDetailsService } from "./services/article-details.service";
import { StatisticsComponent } from './components/statistics/statistics.component';


@NgModule({
  imports: [CommonModule, FormsModule],
  declarations: [ArticleDetailsComponent, CommentsComponent, AdviceComponent, StatisticsComponent],
  providers: [ArticleDetailsService],
  exports: [ArticleDetailsComponent]
})
export class ArticleDetailsModule {}
 