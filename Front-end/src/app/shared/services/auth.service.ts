import { Injectable } from "@angular/core";
import { HttpClient, HttpHeaders } from "@angular/common/http";
import { environment } from "../../../environments/environment";

@Injectable()
export class AuthService {
  constructor(private http: HttpClient) {}
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
}
