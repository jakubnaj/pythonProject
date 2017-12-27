import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { environment } from '../../../environments/environment'
import { Observable } from "rxjs/Observable";

@Injectable()
export class ArticleService {

  constructor(private http: HttpClient) { }


  getArticle(Id): Observable<Object[]> {
    return this.http.get<Object[]>(environment.endpoints.getAdvice);
  }
  
}
 