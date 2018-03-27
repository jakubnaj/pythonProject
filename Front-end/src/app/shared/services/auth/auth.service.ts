import { Injectable, OnInit } from "@angular/core";
import { HttpClient, HttpHeaders } from "@angular/common/http";
import { environment } from "../../../../environments/environment";
import { Observable } from "rxjs/Observable";
import { Subject } from "rxjs/Subject";

@Injectable()
export class AuthService implements OnInit {
  activeName: Subject<string> = new Subject();
  constructor(private http: HttpClient) {}
  ngOnInit() {
  }
  login(username: String, password: String) {
    let headers = new HttpHeaders();
    headers = headers.append(
      "Authorization",
      "Basic " + btoa(username + ":" + password)
    );
    headers = headers.append(
      "Content-Type",
      "application/x-www-form-urlencoded"
    );
    return this.http.get(environment.endpoints.login, { headers: headers });
  }
  saveCredentials(userName: string, password: string) {
    localStorage.setItem("username", userName);
    localStorage.setItem("password", password);
    this.activeName.next(userName);
  }
  getUserName() {
    return localStorage.getItem("username");
  }
  logout() {
    localStorage.removeItem("username");
    localStorage.removeItem("password");
    this.activeName.next("");
  }
}
