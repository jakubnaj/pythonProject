import { Component, OnInit, Input } from "@angular/core";
import { ActivatedRoute } from "@angular/router/router";
import { Advice } from "../../../shared/models/advice";

@Component({
  selector: "app-advice",
  templateUrl: "./advice.component.html",
  styleUrls: ["./advice.component.scss"]
})
export class AdviceComponent implements OnInit {
  @Input() article: Advice;
  ngOnInit() {}
}
