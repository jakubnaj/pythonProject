import { Injectable } from "@angular/core";
import { HttpClient, HttpHeaders } from "@angular/common/http";
import { environment } from "../../../environments/environment";
import { Observable } from "rxjs/Observable";
import { Advice } from "../../shared/models/advice";
import { Comment } from "../models/comment";

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
  createComment(comment: Comment): Observable<any> {
    if (
      !(localStorage.getItem("username") && localStorage.getItem("password"))
    ) {
      throw Observable.throw("Unauthorized");
    }
    let headers = new HttpHeaders();
    headers = headers.append(
      "Authorization",
      "Basic " +
        btoa(
          localStorage.getItem("username") +
            ":" +
            localStorage.getItem("password")
        )
    );
    return this.http.post(
      environment.endpoints.comment,
      { ...comment },
      { headers: headers }
    );
  }

  updateLikes(commentId: number, action: string): Observable<any> {
    if (
      !(localStorage.getItem("username") && localStorage.getItem("password"))
    ) {
      throw Observable.throw("Unauthorized");
    }
    let headers = new HttpHeaders();
    headers = headers.append(
      "Authorization",
      "Basic " +
        btoa(
          localStorage.getItem("username") +
            ":" +
            localStorage.getItem("password")
        )
    );
    return this.http.put(
      environment.endpoints.comment +'/'+ commentId,
      { action },
      { headers: headers }
    );
  }
}
