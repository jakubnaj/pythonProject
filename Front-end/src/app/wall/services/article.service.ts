import { Injectable } from "@angular/core";
import { HttpClient, HttpHeaders } from "@angular/common/http";
import { environment } from "../../../environments/environment";
import { Observable } from "rxjs/Observable";
import { Advice } from "../../shared/models/advice";

@Injectable()
export class ArticleService {
  constructor(private http: HttpClient) {}

  getArticle(Id?): Observable<Advice[]> {
    return this.http.get<Advice[]>(environment.endpoints.advice);
  }

  filterByCategory(advice: Advice[], categoryName: String): Advice[] {
    return advice.filter(item => item.categoryName === categoryName);
  }

  create(advice: Advice): Observable<any> {
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
      environment.endpoints.advice,
      { ...advice },
      { headers: headers }
    );
  }
  sortBySeen(advice: Advice[]) {
    return advice.sort(
      (a, b) => Number(b.viewsQuantity) - Number(a.viewsQuantity)
    );
  }
}
