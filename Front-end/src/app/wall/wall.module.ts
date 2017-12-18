import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { WallContainerComponent } from './components/wall-container.component';
import { ArticleComponent } from './components/article/article.component';
import {RouterModule} from '@angular/router';
import { AddArticleComponent } from './components/add-article/add-article.component';

@NgModule({
  imports: [
    CommonModule,
    RouterModule
  ],
  declarations: [WallContainerComponent, ArticleComponent, AddArticleComponent],
  exports: [WallContainerComponent,AddArticleComponent]
})
export class WallModule { }
