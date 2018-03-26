import { Injectable } from "@angular/core";
import { HttpClient } from "@angular/common/http";
import { environment } from "../../../environments/environment";
import { Observable } from "rxjs/Observable";
import { Advice } from "../../shared/models/advice";

@Injectable()
export class ArticleDetailsService {
  constructor(private http: HttpClient) {}
  getArticle(Id: Number): Observable<Advice[]> {
    return this.http.get<Advice[]>(
      environment.endpoints.getArticle + String(Id)
    );
  }
  getComments(Id: Number): Observable<Comment[]> {
    return this.http.get<Comment[]>(
      environment.endpoints.getAdviceComments + String(Id)
    );
  }
}
