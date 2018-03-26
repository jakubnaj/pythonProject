import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { environment } from '../../../environments/environment'
import { Observable } from "rxjs/Observable";
import { Advice } from '../../shared/models/advice';

@Injectable()
export class ArticleService {

  constructor(private http: HttpClient) { }


  getArticle(Id?): Observable<Advice[]> {
    return this.http.get<Advice[]>(environment.endpoints.getAdvice);
  }

  filterByCategory(advice: Advice[], categoryName: String): Advice[]{
    return advice.filter((item)=> item.CategoryName === categoryName);
  }
}
 