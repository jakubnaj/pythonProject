import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { ArticleDetailsComponent } from './article-details.component';
import { CommentsComponent } from './components/comments/comments.component';
import { AdviceComponent } from './components/advice/advice.component';

@NgModule({
  imports: [
    CommonModule
  ],
  declarations: [ArticleDetailsComponent, CommentsComponent, AdviceComponent],
  exports: [ArticleDetailsComponent]
})
export class ArticleDetailsModule { }
