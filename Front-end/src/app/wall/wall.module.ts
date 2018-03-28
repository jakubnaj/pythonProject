import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { WallContainerComponent } from './components/wall-container.component';
import { ArticleComponent } from './components/article/article.component';
import { RouterModule } from '@angular/router';
import { AddArticleComponent } from './components/add-article/add-article.component';
import { ArticleService } from './services/article.service'
import { HttpClientModule } from '@angular/common/http';
import { FormsModule }   from '@angular/forms';
import { WallCommunicationService } from './services/wall-communication.service';

@NgModule({
  imports: [
    CommonModule,
    RouterModule,
    HttpClientModule,
    FormsModule
  ],
  declarations: [WallContainerComponent, ArticleComponent, AddArticleComponent],
  providers: [ArticleService,WallCommunicationService],
  exports: [WallContainerComponent, AddArticleComponent]
})
export class WallModule { }
