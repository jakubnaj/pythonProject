import { Component, OnInit } from '@angular/core';
import {ArticleService} from '../services/article.service'

@Component({
  selector: 'app-wall-container',
  templateUrl: './wall-container.component.html',
  styleUrls: ['./wall-container.component.scss']
})
export class WallContainerComponent implements OnInit {
  private advices: Array<Object>;

  //Dependency Injection
  constructor(private article: ArticleService) { }

  ngOnInit() {
    this.article.getArticle().subscribe(data => this.advices = data);
  }

}
